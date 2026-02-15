from routes.fallback_routes import fallback_router
from routes.command_routes import command_router
from routes.students_routes import students_router
from routes.tacos_routes import tacos_router
from routes.group_chat_routes import group_chat_router

all_routers = [command_router, group_chat_router, students_router, tacos_router, fallback_router]