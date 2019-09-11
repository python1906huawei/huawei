# 短信应用 SDK AppID
appid = 1400009099  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad"
# 需要发送短信的手机号码
phone_numbers = ["21212313123", "12345678902", "12345678903"]
# 短信模板ID，需要在短信控制台中申请
template_id = 7839  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "腾讯云"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
ssender = SmsSingleSender(appid, appkey)
try:
    result = ssender.send(sms_type, 86, phone_numbers[0],
                          "【腾讯云】您的验证码是: 5678", extend="", ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
