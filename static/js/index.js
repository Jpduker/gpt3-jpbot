function ask(){
    var chat = document.getElementById("chatinp").value;
    document.getElementById('chatq').innerHTML=chat;

    // POST
    fetch('/model', {
        headers: {
        'Content-Type': 'application/json'
        },

        method: 'POST',

        body: JSON.stringify({
            "text": chat
        })
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        text = JSON.parse(text);
        document.getElementById('chatres').innerHTML = text.result;
    });
}