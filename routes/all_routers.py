from routes.fallback_routes import fallback_router
from routes.command_routes import command_router
from routes.students_routes import students_router
from routes.tacos_routes import tacos_router

all_routers = [command_router, students_router, tacos_router, fallback_router]