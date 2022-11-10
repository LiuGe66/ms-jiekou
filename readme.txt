一、Yaml测试用例规范写法：
1.在Yaml用例里必须有一级关键字name,request,validate;同时在request下面必须包含method,url这两个二级关键字。
二、关于接口关联：
    保存中间变量：
    1，此框架仅支持正则表达式和jsonpath提取，实例如下：
      extract:
        access_token: '"access_token":"(.*?)"'
        expires_in: $..expires_in
        access_token1: $..access_token

    使用中间变量：
    1，可以在url,params,data,json,headers中使用，实例如下：
        ${access_token}

