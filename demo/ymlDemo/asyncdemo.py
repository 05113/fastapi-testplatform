def generate():
    i = 0
    while i < 5:
        print("我在这。。")
        xx = yield i  # 注意，python程序，碰到=，都是先从右往左执行
        print(xx)
        i += 1

g = generate()

g.send(None)  # <==> next(g) 第一次启动，执行到yield i（此时i=0），挂起任务，主程序继续往下执行

g.send("lalala")  # 第二次唤醒生成器，从上次的yield i 处继续执行，即往左执行，把lalala赋值给xx后，往下执行，直到下次的yield i（此时i=1），挂起任务

# next(g)  # <==>g.__next__()不常用

