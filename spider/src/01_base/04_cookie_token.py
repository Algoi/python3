'''
    Cookie 与 Token

    Cookie
        浏览器提供的一种数据保存和自动携带机制。
        服务器可通过 Set-Cookie 返回 Cookie。
        后续请求浏览器会自动携带。
        常和 Session 配合实现登录状态。Cookie: sessionid=abc123

        典型流程：
        登录
         ↓
        服务器创建 Session
         ↓
        返回 sessionid
         ↓
        浏览器保存到 Cookie
         ↓
        后续请求自动携带 Cookie
         ↓
        服务器根据 sessionid 找到用户

    Token
        本质是一段“身份凭证”。
        通常登录成功后由服务器返回。
        客户端自己保存，并主动携带。
        常放在 Authorization 请求头中。比如：Authorization: Bearer xxxxx

    典型流程：
    登录
     ↓
    服务器生成 Token
     ↓
    客户端保存
     ↓
    请求 API 时携带 Token
     ↓
    服务器验证 Token

    两者区别
    | 对比        | Cookie + Session     | Token                     |
    |------------ |----------------------|---------------------------|
    | 凭证常见位置 | Cookie               | Authorization             |
    | 是否自动发送 | 浏览器自动            | 客户端主动添加            |
    | 服务端状态   | 通常保存 Session      | JWT 等可做到无状态        |
    | 常见场景     | 网页系统              | API、App、前后端分离      |
    | 跨客户端使用 | 浏览器最方便           | 更通用                    |
'''

'''
    前后端分离为什么常用 Token 而不是 Cookie + Session ?

    不是因为 Cookie 不能使用只是 Token 通常更方便，因为：
        Web
        App
        小程序
        桌面客户端
        第三方程序
            ↓
        都可以统一使用 Token
    而且调用 API 时非常直观：Authorization: Bearer token
'''

'''
    爬虫中：
    1、如果存在 Cookie: sessionid=xxx，通常是 Cookie + Session 的登录状态，爬虫可以直接携带 Cookie 访问。
    2、如果存在 Authorization: Bearer xxx，通常是 Token 的登录状态，爬虫可以直接携带 Token 访问。
    3、如果存在 X-CSRFToken: xxx，防 CSRF 请求伪造。不是登录 Token。
        CSRF 全称是 Cross-Site Request Forgery，跨站请求伪造。浏览器在请求某个网站时，会自动携带这个网站的 Cookie。
'''