#from shipit_bot_sa.workflow import PulseWorkflow


def main():

    import asyncio

    async def hello_world():
        print("Hello World!")

    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(hello_world())
    loop.close()

    return

    w = PulseWorkflow()
    w.run()


if __name__ == '__main__':
    main()
