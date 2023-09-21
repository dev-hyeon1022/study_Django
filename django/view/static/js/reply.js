const replyService = (function(){
    async function getList(){
        const response = await fetch(`/replies/list/${post_id}`);
        const replies = await response.json()
        return replies;
    }

    async function write(reply_content){
        const response = await fetch("/replies/write/", {
            method: 'post',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: JSON.stringify({post_id: post_id, reply_content: reply_content})
        });
        // response.catch((error) => {})
    }

    return {getList: getList, write: write};
})()

const view = (function(){
    function showList(replies){
        const table = document.getElementById("replies");

        if(replies.length != 0){
            let text = "";
            console.log(replies);
            replies.forEach((reply) => {
                text += `
                    <tr>
                        <td>${reply.id}</td>
                        <td>${reply.member_name}</td>
                        <td>${reply.reply_content}</td>
                    </tr>
                `
            });

            table.innerHTML = text;
        }

    }

    return {showList: showList};
})()


replyService.getList().then(view.showList);

document.getElementById("write").addEventListener("click", () => {
    const reply_content = document.getElementById("reply-content").value;
    replyService.write(reply_content).then(() => {replyService.getList().then(view.showList);});

})














