<style>
    .article{
        font-family: 맑은고딕, Malgun Gothic, dotum, gulim, sans-serif;
        font-size: 20pt;
        padding:10vw;
        text-align: center;
        display: flex;
    }

    .wbg{
        background-color: #ffffff;
    }

    .gbg{
        background-color: #edeff2;
    }

    .article img {
        display: inline-block;
        max-width: 500px;
        width: 20vw;
        margin-left: 4vw;
        margin-right: 4vw;
    }

    .article .text {
        display: inline-block;
        width: 50vw;
    }

    .contents{
        display: flex;
        align-items: center;
    }
</style>
<script>
</script>

<div class="article wbg" id="article1">
    <div class="contents">
        <img src="./static/pompeii.png" alt=":)">
        <div class="text">
            <span>이불 안도 위험해!</span><br>
            하이 폼페이! 폼페이는 여러분과 소통하는<br> 재난 안전 AI 스피커예요. <br>
        </div>
    </div>
</div>
<div class="article gbg" id="article2">
    <div class="contents"> 
        <div class="text">
            폼페이에서 재난 관련 퀴즈를 풀어보세요!<br>
            여러 재난에 관련된 다양한 퀴즈를 풀어볼 수 있어요.
        </div>
        <img src="./static/quiz.png" alt=";(">
    </div>
</div>
<div class="article wbg" id="article3">
    <div class="contents">
        <img src="./static/news.png" alt=":)">
        <div class="text">
            폼페이에게 국내 재난 관련 최신 뉴스를 물어보세요!<br>
            폼페이는 재난 관련 뉴스를 매일 수집하여 여러분께 전달해요.
        </div>
    </div>
</div>
<div class="article gbg" id="article4">
    <div class="contents">
        <div class="text" style="font-size:19pt">
            폼페이는 TTS/STT와 KoBERT Embedder로 여러분과 소통합니다.<br>
            폼페이와의 대화 내역은 <br>svelte 반응형 인터페이스를 통해 여러분에게 보여집니다.
        </div>
        <img src="./static/tech.png" alt=";(">
    </div>
</div>