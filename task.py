import asyncio
import time

list_email_address = ['a', 'b', 'c', 'd', 'e']

async def todo(to):
	print('Sent Email to {} at time: {}'.format(to, time.strftime('%X')))

async def main():
	for i in list_email_address:
		task = asyncio.create_task(todo(i))
	done, pending = await asyncio.wait({task})
	print("Pending Email: ", pending)
	print("Sent Email: ", done)

if __name__ == '__main__':
	asyncio.run(main())
	print('Complete')
