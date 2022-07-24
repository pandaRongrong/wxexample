import hashlib
import web
import receive
import reply

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "test"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    print(replyMsg)
                    return replyMsg.send()
                else:
                    return replyMsg().send()
            else:
                print("暂且不处理")
                return replyMsg().send()
        except Exception as Argment:
            return Argment
        
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "czrtoken"

            list = [token, timestamp, nonce]
            list.sort()
            shal = hashlib.sha1()
            map(shal.update, list)
            hashcode = shal.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            return echostr
            #if hashcode == signatrue:
            #    return echostr
            #else:
            #    return ""
        except Exception as Argument:
            return Argument
