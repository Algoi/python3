'''
    爬虫是利用程序进行批量爬取网上的公开信息，也就是前端显示的数据信息。
    因为信息是完全公开的，所以是常规合法的！！！

    合法的爬虫
        公开的数据，没有标识不可爬取
        不影响别人服务器
        不影响的业务
    不合法的爬虫
        用户数据
        部分网站、APP数据超过指定数量
        明文规定不让爬取
        在域名后加上 /robots.txt 查看
        页面上标明
        影响业务
        影响服务器
        类似DDOS攻击的问题
'''

'''
    /robots.txt 示例（不是所有网站都有的）

    https://www.baidu.com/robots.txt 返回如下页面数据：
        User-agent: Googlebot
        Disallow: /baidu
        Disallow: /s?
        Disallow: /shifen/
        Disallow: /homepage/
        Disallow: /cpro
        Disallow: /ulink?
        Disallow: /link?
        Disallow: /home/news/data/
        Disallow: /bh

        ...

        User-agent: Sogou web spider
        Disallow: /baidu
        Disallow: /s?
        Disallow: /shifen/
        Disallow: /homepage/
        Disallow: /cpro
        Disallow: /ulink?
        Disallow: /link?
        Disallow: /home/news/data/
        Disallow: /bh

'''

'''
    反爬：不希望让别人爬取自己网站的数据，通过一系列手段进行限制，手段有：
        合法检测：请求校验(useragent，referer，接口加签 ，等)
        验证码：识别文字、做题、滑动等
        小黑屋：IP/用户限制请求频率，或者直接拦截
        投毒：反爬虫高境界可以不用拦截，拦截是一时的，投毒返回虚假数据，可以误导竞品决策

    反反爬：破解掉反爬手段，再获取其数据。
'''

'''
    爬虫基本思路
        1. 基本流程
            1.1 目标数据：想要什么数据
            1.2 数据来源：数据从哪里来，即某个地址
            1.3 结构分析：具体数据在哪里（App、网站），如何展示数据
            1.4 实现构思
            1.5 编码实现
        2. 基本手段
            2.1 破解请求限制
                * 请求头设置，如 User-Agent、Referer、Cookie、Host、Origin、X-Requested-With 等
                * 控制请求频率，避免被封 IP
                * 代理 IP，避免被封 IP
                * 签名/加密参数从 html/cookie/js 中获取
            2.2 破解登录授权，请求需要携带 cookie、token 等信息
            2.3 破解验证码，适用第三方库识别验证码
        3. 解析数据
            3.1 HTML DOM 解析：正则匹配、XPath 等第三库解析 html 结构获取数据
            3.2 数据字符串：转 JSON/XML 对象进行解析
'''