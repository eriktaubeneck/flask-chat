var inbox = new ReconnectingWebSocket("ws://"+ location.host + "/receive");
var outbox = new ReconnectingWebSocket("ws://"+ location.host + "/submit");

add_message = function(data) {
    $("#chat-text").append("<div class='panel panel-default'><div class='panel-heading'>" + $('<span/>').text(data.handle).html() + "</div><div class='panel-body'>" + $('<span/>').text(data.text).html() + "</div></div>");
    $("#chat-text").stop().animate({
        scrollTop: $('#chat-text')[0].scrollHeight
    }, 800);
};

$.getJSON("/past_chats", function(messages) {
    $.each(messages, function(i, message) {
        var data = JSON.parse(message);
        add_message(data);
    });
});



inbox.onmessage = function(message) {
    var data = JSON.parse(message.data);
    add_message(data);
};


$("#input-form").on("submit", function(event) {
      event.preventDefault();
      var handle = $("#input-handle")[0].value;
      var text   = $("#input-text")[0].value;
      outbox.send(JSON.stringify({ handle: handle, text: text }));
      $("#input-text")[0].value = "";
    });
