#This is a tcp server using asyncio
#importing asyncio so that server can perform asynchronous networking - handle many clients without freezing
import asyncio

#defining what happens when client connects
#asynchonous function defined with two parameters reader, and writer
async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    print("connected: ", addr)

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()
            
            print(f"{addr} {message}")

            response = f"Server recieved: {message}"

            writer.write(response.encode())

            await writer.drain()

    except Exception as e:
         print(f"Error with {addr}: {e}")

    finally:
        print(f"{addr} disconnected")
        writer.close()
        await writer.wait_close()

async def main():
    server = await asyncio.start_server(handle_client, "0.0.0.0", 5000)
    print("Async server is running on port 5000")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
        asyncio.run(main())
