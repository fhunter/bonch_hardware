%include header
%import settings
%from utils import json2tree
<h1>Сравнение аппаратуры компьютера {{hostname}}</h1>
<div class="row">
<div class="column">
<h2>Версия 1<br/>{{computer1.date}}</h2>
{{! json2tree(computer1.hardware, diff=diff, lr='l' )}}
</div>
<div class="column">
<h2>Версия 2<br/>{{computer2.date}}</h2>
{{! json2tree(computer2.hardware, diff=diff, lr='r' )}}
</div>
</div>

%include footer
