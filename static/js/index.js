function ask(){
    var chat = document.getElementById("chatinp").value;
    let query =chat;
    let queryHtml = ' <p class= "chatq"<span>' + query +'</span><p>'
    $("#chatq").append(queryHtml)

    
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
        let response = text.result;
        let responseHtml = ' <p class= "responses"<span>' + response +'</span><p>';
        $("#responses").append(responseHtml);
        
    });
}

