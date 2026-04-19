from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Birthday Surprise 🎂</title>

<style>
body{
font-family: Arial;
background: linear-gradient(135deg,#ff9a9e,#fad0c4);
display:flex;
justify-content:center;
align-items:center;
height:100vh;
margin:0;
}

.container{
background:white;
padding:40px;
border-radius:15px;
text-align:center;
max-width:400px;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

button{
padding:12px 20px;
border:none;
background:#ff4081;
color:white;
border-radius:8px;
cursor:pointer;
margin-top:20px;
}

input{
padding:10px;
width:100%;
margin-top:20px;
border-radius:8px;
border:1px solid #ddd;
}

.hidden{
display:none;
}

h1{
color:#ff4081;
}
</style>

</head>

<body>

<div class="container">

<h1>🎉 Birthday Surprise 🎉</h1>

<div id="step1">
<p>Kripya apna naam bataye 😝</p>
<input id="name" placeholder="Your Name">
<button onclick="nextStep()">Continue</button>
</div>

<div id="step2" class="hidden">
<p id="hello"></p>
<button onclick="step3()">Continue</button>
</div>

<div id="step3" class="hidden">
<p>Aaj kaafi special day hai 🤭</p>
<p>Because someone very cute was born today...</p>
<p>Guess who? 😏</p>
<button onclick="step4()">Reveal</button>
</div>

<div id="step4" class="hidden">
<h2>It's YOU, my kuchipuu 😝</h2>
<button onclick="step5()">Continue</button>
</div>

<div id="step5" class="hidden">
<h3>Reasons why you're awesome:</h3>
<ul>
<li>You make my day better</li>
<li>You make me jealous 😭 but still care</li>
<li>You gave chocolates to me</li>
<li>You made handmade cards for me 🤌</li>
<li>You're literally THE sweetest person 😭</li>
</ul>
<button onclick="step6()">Open Gift 🎁</button>
</div>

<div id="step6" class="hidden">
<p>Pick a Gift 🎁</p>
<button onclick="gift(1)">1</button>
<button onclick="gift(2)">2</button>
<button onclick="gift(3)">3</button>
</div>

<div id="step7" class="hidden">
<h2 id="giftText"></h2>
<button onclick="step8()">Continue</button>
</div>

<div id="step8" class="hidden">
<h1>🎂 HAPPY BIRTHDAY 🎂</h1>
<p>Thank you for being in my life</p>
<p>- From someone who likes annoying you 🫶</p>
</div>

</div>

<script>

function nextStep(){
let name=document.getElementById("name").value
document.getElementById("hello").innerText="Hello "+name+" 👀"
document.getElementById("step1").style.display="none"
document.getElementById("step2").style.display="block"
}

function step3(){
document.getElementById("step2").style.display="none"
document.getElementById("step3").style.display="block"
}

function step4(){
document.getElementById("step3").style.display="none"
document.getElementById("step4").style.display="block"
}

function step5(){
document.getElementById("step4").style.display="none"
document.getElementById("step5").style.display="block"
}

function step6(){
document.getElementById("step5").style.display="none"
document.getElementById("step6").style.display="block"
}

function gift(n){

let messages={
1:"You won: 1 free chocolate 🍫",
2:"You won: Unlimited bullying rights 😝",
3:"You won: One full day hangout 😙"
}

document.getElementById("giftText").innerText=messages[n]

document.getElementById("step6").style.display="none"
document.getElementById("step7").style.display="block"

}

function step8(){
document.getElementById("step7").style.display="none"
document.getElementById("step8").style.display="block"
}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)