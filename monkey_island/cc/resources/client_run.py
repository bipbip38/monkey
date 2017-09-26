from flask import request, jsonify
import flask_restful

from cc.services.node import NodeService

__author__ = 'itay.mizeretz'


class ClientRun(flask_restful.Resource):
    def get(self):
        client_ip = request.remote_addr
        if client_ip == "127.0.0.1":
            monkey = NodeService.get_monkey_island_monkey()
        else:
            monkey = NodeService.get_monkey_by_ip(client_ip)
        NodeService.update_dead_monkeys()
        if monkey is not None:
            is_monkey_running = not monkey["dead"]
        else:
            is_monkey_running = False

        return jsonify(is_running=is_monkey_running)
