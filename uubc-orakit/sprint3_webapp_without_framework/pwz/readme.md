# 迭代3：提供网页客户端（Web开发）（不使用框架，造轮子）

迭代3从迭代2的C/S架构（Client/Server）客户端“升级”为B/S架构（Browser/Server）架构的网页端程序，  
通过造轮子实现了从前端页面发出请求、http请求处理、路由到服务代码给出响应，最终反显前端整套流程。

迭代3使用Html、JavaScript、Java实现，最终交付物汇总如下:
* PRD：[OraKit Sprint 3 PRD](./prd)
* OraKit3.0：
  1. [本次迭代说明文档](./orakit_sprint_3/readme)
  2. [Code~ 应用主页html及js代码](./orakit_sprint_3/static_site/index.html)
  3. [Code~ Http服务器及路由函数](./orakit_sprint_3/http_server/HttpServer.java)
  4. [Code~ 后台服务代码（Mock）](./orakit_sprint_3/service_impl/ChatBot.java)