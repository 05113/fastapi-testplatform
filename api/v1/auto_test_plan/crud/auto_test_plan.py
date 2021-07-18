from sqlalchemy.orm import Session
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import threading
from typing import List

# from main import app
from db.session import DbSession
from models.auto_test_plan import AutoTestPlan
from models.auto_test_plan_job import AutoTestPlanJob
from models.auto_test_plan_job_detail import AutoTestPlanJobDetail
from ..schemas import auto_test_plan_schemas
from api.v1.auto_project_api_case.crud.auto_project_api_case import crud_project_case


print('mmmmmmmmmm')
executor = ThreadPoolExecutor(max_workers=10)

lock = threading.Lock()


class CRUDTestPlan:
    def __init__(self):
        self.model = AutoTestPlan
    def add_test_plan(
            self , * , db : Session , project_id , obj_in : auto_test_plan_schemas.TestPlanCreate
    ):
        obj_data = AutoTestPlan(test_plan_name = obj_in.test_plan_name ,
                                test_plan_describe = obj_in.test_plan_describe ,
                                test_plan_host = obj_in.test_plan_host ,
                                test_plan_port = obj_in.test_plan_port ,
                                test_plan_api_group = obj_in.test_plan_api_group ,
                                project_id = project_id)
        lock.acquire()
        db.add(obj_data)
        db.commit()
        lock.release()
    def update_test_plan(
            self , * ,db : Session , test_plan_id : int , obj_in : auto_test_plan_schemas.TestPlanUpdate
    ):
        # todo 修改测试计划
        if obj_in.test_plan_name is not None:
            db.query(self.model).filter(self.model.id == test_plan_id).update({self.model.test_plan_name : obj_in.test_plan_name})
        if obj_in.test_plan_describe is not None:
            db.query(self.model).filter(self.model.id == test_plan_id).update({self.model.test_plan_describe : obj_in.test_plan_describe})
        if obj_in.test_plan_host is not None:
            db.query(self.model).filter(self.model.id == test_plan_id).update({self.model.test_plan_host : obj_in.test_plan_host})
        if obj_in.test_plan_port is not None:
            db.query(self.model).filter(self.model.id == test_plan_id).update({self.model.test_plan_port : obj_in.test_plan_port})
        if obj_in.test_plan_api_group is not None:
            db.query(self.model).filter(self.model.id == test_plan_id).update({self.model.test_plan_api_group : obj_in.test_plan_api_group})
        pass
    def get_test_plan_by_id(
            self , * , db : Session , test_plan_id : int
    ) -> AutoTestPlan:

        test_plan_obj = db.query(self.model).filter(self.model.id == test_plan_id).first()
        return test_plan_obj

    def run_test_plan(
            self , *  , test_plan_id : int
    ):
        k = executor.submit(self._test_plan_thread  , test_plan_id)
        # self._test_plan_thread(db = db , test_plan_id=test_plan_id)
        return 1
    def _test_plan_thread(self  , test_plan_id):
        db = DbSession()
        self._do_test_plan(db = db , test_plan_id = test_plan_id)
    def _do_test_plan(self,db,test_plan_id):
        success_count = 0
        fail_count = 0
        test_plan_obj = self.get_test_plan_by_id(db = db , test_plan_id = test_plan_id)
        test_plan_job_id = self._create_test_plan_job(db = db , test_plan_id = test_plan_id)

        test_plan_api_group = test_plan_obj.test_plan_api_group
        for item in range(len(test_plan_api_group)):
            self._create_test_plan_job_detail(db = db ,test_plan_job_id = test_plan_job_id , api_id = test_plan_api_group[item])

        print('create job_detail success')

        # 开始做任务

        # 修改状态为doing
        self._update_job_state(db = db , test_plan_job_id = test_plan_job_id , state = 'DOING')

        # 遍历test_plan_api_group
        for item in range(len(test_plan_api_group)):
            # 跑api的所有case,得出结果,如果api的任意case失败,那么这个api结果即为false
            api_result = self._start_run_job(db = db,

                                             test_plan_job_id = test_plan_job_id,
                                             test_plan_host = test_plan_obj.test_plan_host,
                                             test_plan_port = test_plan_obj.test_plan_port,
                                             api_id = test_plan_api_group[item])


            if api_result:
                success_count = success_count + 1
                self._update_success_count(db = db ,test_plan_job_id = test_plan_job_id , success_count = success_count)
            else:
                fail_count = fail_count + 1
                self._update_fail_count(db = db ,test_plan_job_id = test_plan_job_id , fail_count = fail_count)
        if fail_count == 0:
            self._update_test_plan_result(db = db , test_plan_job_id = test_plan_job_id , test_plan_result = True)
        else:
            self._update_test_plan_result(db = db , test_plan_job_id = test_plan_job_id , test_plan_result = False)

        self._update_job_state(db = db , test_plan_job_id = test_plan_job_id , state = 'DONE')


        pass
    def _create_test_plan_job(
            self ,db : Session ,test_plan_id
    ):
        create_obj = AutoTestPlanJob(test_plan_id = test_plan_id,
                                     state = "init",
                                     success_count = 0,
                                     fail_count = 0)
        db.add(create_obj)
        db.commit()
        test_plan_job_id = create_obj.id
        return test_plan_job_id
    def _create_test_plan_job_detail(
            self , db : Session , test_plan_job_id : int  , api_id : int
    ):
        print(7.1)
        project_case_list = crud_project_case.get_project_case(db = db , project_api_id = api_id)

        for item in range(len(project_case_list)):

            creat_job_detail_obj = AutoTestPlanJobDetail(test_plan_job_id = test_plan_job_id,
                                                         api_id = api_id,
                                                         api_group_id = project_case_list[item]['id'])
            db.add(creat_job_detail_obj)
            db.commit()
        print(7.2)
    def _start_run_job(
            self , db , test_plan_job_id , test_plan_host , test_plan_port , api_id
    ):

        api_result = True
        # job_detail组成:由job中的api_group生成，每个api含有多个case,每个case_detail作为一条记录
        # 获取job中api_group的每个api的所有case_detail的list
        job_detail_list_by_api = self._get_job_detail_by_test_plan_job_id_and_api_id(db = db ,
                                                                                  test_plan_job_id = test_plan_job_id ,
                                                                                  api_id = api_id)
        # 遍历case_detail_list
        for job_detail in range(len(job_detail_list_by_api)):
            # run case获取结果
            new_api_result = self._do_job_detail(db = db ,
                                                 job_detail_id = job_detail_list_by_api[job_detail].id,
                                                 job_detail_api_group_id = job_detail_list_by_api[job_detail].api_group_id,
                                                 test_plan_host = test_plan_host,
                                                 test_plan_port = test_plan_port)
            # 如果api的所有case都为true,那么这个api为true
            api_result = api_result and new_api_result

        return api_result


    def _do_job_detail(
            self , db , job_detail_id , job_detail_api_group_id , test_plan_host , test_plan_port
    ) -> bool:
        assert_result , assert_result_list = crud_project_case.run_project_case(db = db ,
                                                                                project_case_id = job_detail_api_group_id ,
                                                                                api_host = test_plan_host ,
                                                                                api_port = str(test_plan_port))
        self._update_job_detail_response_body(db = db ,
                                              test_plan_job_detail_id = job_detail_id,
                                              response_body = assert_result_list[0])
        self._update_job_detail_result(db = db,
                                       test_plan_job_detail_id = job_detail_id,
                                       api_group_result = assert_result)
        api_result = assert_result

        return api_result

    # 获取job的每个api的所有case_detail
    def _get_job_detail_by_test_plan_job_id_and_api_id(
            self , db : Session , test_plan_job_id : int , api_id : int
    ) -> List:
        job_detail_list = db.query(AutoTestPlanJobDetail).filter(AutoTestPlanJobDetail.test_plan_job_id == test_plan_job_id , AutoTestPlanJobDetail.api_id == api_id).all()

        return job_detail_list

    def _update_job_state(
            self,db:Session , test_plan_job_id , state
    ):
        db.query(AutoTestPlanJob).filter(AutoTestPlanJob.id == test_plan_job_id).update(
            {AutoTestPlanJob.state: state})
        lock.acquire()
        db.commit()
        lock.release()

    def _update_success_count(
            self , db : Session , test_plan_job_id : int , success_count : int
    ):
        db.query(AutoTestPlanJob).filter(AutoTestPlanJob.id == test_plan_job_id).update(
            {AutoTestPlanJob.success_count : success_count})

        lock.acquire()
        db.commit()
        lock.release()

    def _update_fail_count(
            self , db : Session , test_plan_job_id : int , fail_count : int
    ):
        db.query(AutoTestPlanJob).filter(AutoTestPlanJob.id == test_plan_job_id).update(
            {AutoTestPlanJob.fail_count : fail_count})
        lock.acquire()
        db.commit()
        lock.release()
    def _update_test_plan_result(
            self , db : Session , test_plan_job_id : int ,  test_plan_result
    ):
        db.query(AutoTestPlanJob).filter(AutoTestPlanJob.id == test_plan_job_id).update(
            {AutoTestPlanJob.test_plan_result : test_plan_result})
        lock.acquire()
        db.commit()
        lock.release()



    def _update_job_detail_response_body(
            self,db:Session , test_plan_job_detail_id , response_body
    ):
        db.query(AutoTestPlanJobDetail).filter(AutoTestPlanJobDetail.id == test_plan_job_detail_id).update(
            {AutoTestPlanJobDetail.response_body: response_body})
        lock.acquire()
        db.commit()
        lock.release()
    def _update_job_detail_result(
            self,db:Session , test_plan_job_detail_id , api_group_result
    ):
        db.query(AutoTestPlanJobDetail).filter(AutoTestPlanJobDetail.id == test_plan_job_detail_id).update(
            {AutoTestPlanJobDetail.api_group_result: api_group_result})
        lock.acquire()
        db.commit()
        lock.release()



crud_test_plan = CRUDTestPlan()
