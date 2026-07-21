# import asyncio
# import traceback

# from app.main import run


# if __name__ == "__main__":

#     try:

#         asyncio.run(
#             run()
#         )

#     except Exception:

#         traceback.print_exc()

#         input(
#             "\nPresiona ENTER para cerrar..."
#         )



import traceback


try:

    from gui.app import JarvisApp

    print("1 - Import JARVIS OK")


    jarvis = JarvisApp()

    print("2 - Ventana creada")


    jarvis.run()


except Exception:

    traceback.print_exc()

    input("\nENTER para salir...")