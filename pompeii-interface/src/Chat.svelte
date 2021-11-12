<style>
	#chat_bg {
		box-sizing: border-box;
		display: flex;
		height: 110vh;
		background-color:#edeff2;
	}
	#chat_frame {
		position: absolute;
		width: 85% ;
		max-width: 800px;	
		height: 700px;
		border-radius: 10px;
		left: 50%;
		top: 450px;
		transform: translateX(-50%) translateY(-50%);
		box-shadow: 0 10px 20px rgb(0 0 0 / 15%);
		background-color: #f8f8f8;
		overflow: hidden;
	}

	#top {
		background-color: rgb(250, 245, 245);
		width: 100%;
		padding: 20px 0 15px;
		box-shadow: 0 1px 30px rgb(0 0 0 / 10%);
	}

	#title {
		font-weight: bold;
		text-align: center;
		color: #8f8989;
		font-size: 20px;
	}

	ul {
		display: block;
		list-style-type: disc;
		margin-block-start: 1em;
		margin-block-end: 1em;
		margin-inline-start: 0px;
		margin-inline-end: 0px;
		padding-inline-start: 40px;
	}

	#messages {
		position: relative;
		list-style: none;
		padding: 20px 10px 0 10px;
		margin: 0;
		height: 520px;
		overflow-y : scroll;
		scroll-behavior: smooth;
	}

	#messages .message {
		clear: both;
		overflow: hidden;
		margin-bottom: 20px;
		transition: all 0.5s linear;
		opacity: 0;
	}

	#messages .message.left .avatar {
		/* background-color: #f5886; */
		float: left;
	}

	#messages .message.left .avatar img {
		width: 68px;	
	}

	#messages .message.left .text_wrapper {
		background-color: #ffe6cb;
		margin-left: 20px;
		white-space: pre;
	}

	#messages .message.left .text_wrapper::after, #messages .message.left .text_wrapper::before {
		right: 100%;
		border-right-color: #ffe6cb;
	}

	#messages .message.left .text {
		color: #c48843;
	}

	#messages .message.right .avatar {
		background-color: #fdbf68;
		float: right;
	}

	#messages .message.right .text_wrapper {
		background-color: #c7eafc;
		margin-right: 20px;
		float: right;
	}

	#messages .message.right .text_wrapper::after, #messages .message.right .text_wrapper::before {
		left: 100%;
		border-left-color: #c7eafc;
	}

	#messages .message.right .text {
		color: #45829b;
	}
	#messages .message.appeared {
		opacity: 1;
	}
	#messages .message .avatar {
		width: 60px;
		height: 60px;
		border-radius: 50%;
		display: inline-block;
	}
	#messages .message .text_wrapper {
		display: inline-block;
		padding: 20px;
		border-radius: 6px;
		width: 80%;
		min-width: 100px;
		position: relative;
	}
	#messages .message .text_wrapper::after, #messages .message .text_wrapper:before {
		top: 18px;
		border: solid transparent;
		content: " ";
		height: 0;
		width: 0;
		position: absolute;
		pointer-events: none;
	}
	#messages .message .text_wrapper::after {
		border-width: 13px;
		margin-top: 0px;
	}
	#messages .message .text_wrapper::before {
		border-width: 15px;
		margin-top: -2px;
	}
	#messages .message .text_wrapper .text {
		font-size: 18px;
		font-weight: bolder;
		white-space: pre-wrap;
		word-break: break-all;
	}

	#bottom {
			position: relative;
			width: 100%;
			background-color: #fff;
			padding: 20px 20px;
			position: absolute;
			bottom: 0;
	}
	#bottom .message_input_wrapper {
		display: inline-block;
		height: 50px;
		border-radius: 25px;
		border: 1px solid #bcbdc0;
		width: 90%;
		position: relative;
		padding: 0 20px;
	}
	#bottom .message_input_wrapper .message_input {
		border: none;
		height: 100%;
		box-sizing: border-box;
		width: 90%;
		position: absolute;
		outline-width: 0;
		color: gray;
	}
</style>

<script>
	import { fade } from 'svelte/transition';
	import { beforeUpdate, afterUpdate, onMount } from 'svelte';
	import Waiting from "./Waiting.svelte"

	let Messages = [
		{side: 'left', text: "안녕하세요! :)"}
	]
	let autoScroll;
	let div;
	let txt = ``;

	beforeUpdate(() => {
		autoScroll = div && (div.offsetHeight + div.scrollTop) > (div.scrollHeight - 20);
	});

	afterUpdate(() => {
		if (autoScroll) div.scrollTo(0, div.scrollHeight);
	});

	function newText(text, side) {
		Messages.push({
			side, text
		});
		Messages = Messages;
		txt = "";
	}

	function addText(text) {
		Messages.at(-1).text += " " + text;
		Messages = Messages;
		txt = "";
	}

	// var socket = new WebSocket("ws://localhost:3000");
	var socket = new WebSocket("ws://192.168.0.69:3000");
	socket.onopen = () => {
		console.log("ㅎㅇ 연결성공함");
		socket.send(".");
	};

	socket.onmessage = (event) => {
		socket.send(".");
		let message = JSON.parse(event.data);
		console.log(message);

		if(message.side == "add") {
			addText(message.text);
		} else {
			newText(message.text, message.side);
		}
	};
</script>

<div id="chat_bg">
	<div id="chat_frame">
		<div id="top">
			<div id="title">Pompeii</div>
		</div>
		<ul id="messages" bind:this={div}>
			{#each Messages as message}
				{#if message.side == 'left'}
					<li class="message left appeared" transition:fade="{{duration: 300 }}">
						<div class="avatar">
							<img src="./static/pompeii.png" alt=":)">
						</div>
						<div class="text_wrapper">
							<div class="text">
								{#if message.text != ""}
									<span></span>
									{message.text}
								{:else}
									<Waiting/>
								{/if}
							</div>
						</div>
					</li>
				{:else}
					<li class="message right appeared" transition:fade="{{duration: 300 }}">
						<div class="avatar"></div>
						<div class="text_wrapper">
							<div class="text">
								{#if message.text != ""}
									{message.text}
								{:else}
									<Waiting/>
								{/if}
							</div>
						</div>
					</li>
				{/if}
			{/each}
		</ul>
		<div id="bottom">
			<div class="message_input_wrapper"><input bind:value={txt} class="message_input" placeholder="..." disabled></div>
		</div>
	</div>
</div>
