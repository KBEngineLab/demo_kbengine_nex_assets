# async_dispatcher.py
import asyncio
import threading

print("import")
loop = asyncio.new_event_loop()

init = False


def start_loop():
    asyncio.set_event_loop(loop)
    print("[Python] Event loop started")
    loop.run_forever()

# if not init:
#     启动事件循环线程
threading.Thread(target=start_loop, daemon=True).start()
    # init = True
pending_tasks = []

def submit_coroutine(coro):
    print("[Python] Submitting coroutine:", coro)
    print("[Python] Loop running?", loop.is_running())
    print("[Python] Loop closed?", loop.is_closed())
    """线程安全提交 coroutine 到事件循环中"""
    print("[Python] Event loop started111")

    try:
        future = asyncio.run_coroutine_threadsafe(coro, loop)

        def on_done(fut):
            try:
                result = fut.result()
                print("[Python] ✅ Coroutine completed:", result)
            except Exception as e:
                print("[Python] ❌ Coroutine raised exception:", e)

        future.add_done_callback(on_done)
        pending_tasks.append(future)  # 防止被 GC
        print("[Python] Future:", future)

    except Exception as e:
        print("[Python] Error in submit_coroutine:", e)