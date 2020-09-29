#!/usr/bin/python3
print("content-type: text/html")
print()

print("""<DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<!link rel="stylesheet" type="text/css" href="style.css">
<style>
h1 {
            color: green;
        }

        .buttonIn {
            width: 300px;
            position: relative;
        }

        input {
            margin: 0px;
            padding: 0px;
            width: 100%;
            outline: none;
            height: 30px;
            border-radius: 5px;
        }

        button {
            position: absolute;
            top: 0;
            border-radius: 5px;
            right: 0px;
            z-index: 2;
            border: none;
            top: 2px;
            height: 30px;
            cursor: pointer;
            color: white;
            background-color: #1e90ff;
            transform: translateX(2px);
        }
    </style>
<title>JS methods</title>

</head>
<body>
<body>	
        <center>
        <h1>IIEC_RISE</h1>
        <b>Simple Web Api chatbot </b>
        <br>
        <br>
        <div class="buttonIn">
            <form action="http://192.168.1.2/cgi-bin/iiec.py">
                <input type="text" name="x" id="speechToText" placeholder="Type or Speak Something" onclick="record()">
                <button type="button" onclick="record()"><img
                        src="https://www.flaticon.com/svg/static/icons/svg/60/60955.svg" style="width:20px;height:13px;"
                        onclick="record()"></button>
                <input type="submit">
            </form>
        </div>
        <center>


<script type="text/javascript">
function record() {
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";

    recognition.onresult = function (event) {
        // console.log(event);
        document.getElementById('speechToText').value = event.results[0][0].transcript;
    }
    recognition.start();

}
window.addEventListener('load', () => {
    const button = document.querySelector('#clear');
    button.addEventListener('click', () => {
        document.querySelector('#enter').value = "";
    });
                }); 
speaks = [{"name": "Veena","lang": "en-US"}];

const msg = new SpeechSynthesisUtterance();
msg.volume = 1; // 0 to 1
msg.rate = 1; // 0.1 to 10
msg.pitch = 1.2; // 0 to 2
msg.text  = "Hello naman";


const voice = speaks[0]; //47
console.log(`Voice: ${voice.name} and Lang: ${voice.lang}`);
msg.voiceURI = voice.name;
msg.lang = voice.lang;


//speechSynthesis.speak(msg);

</script>
</body>
</html>

""")


import cgi
import cgitb
import subprocess as sp
cgitb.enable()

y = cgi.FieldStorage()
cmd = y.getvalue("x")
#print(cmd)

def speak(string):
	print("<script type='text/javascript'>msg.text  = '{}';speechSynthesis.speak(msg);</script>".format(string))

speak("working")


print(sp.getoutput(cmd))
print("<br>")
print(sp.getoutput("id c"))
speak("hello")
#print("<script>document.getElementsByTagName('HTML')[0].innerHTML="";</script>	")
