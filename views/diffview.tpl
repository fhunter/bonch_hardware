%include header
%import settings
%from utils import json2tree
<h1>Сравнение аппаратуры компьютера {{hostname}}</h1>
<a href="{{settings.PREFIX}}/computer/{{hostname}}">Обратно к {{hostname}}</a>
<div class="row">
<div class="column">
<h2>Версия {{start}}<br/>{{computer1.date}}</h2>

%if start > 0:
    <a href="{{settings.PREFIX}}/computer/{{hostname}}/{{start-1}}/{{end}}">&larr;</a>
%end
&nbsp;{{start}}&nbsp;
%if start < length-1:
    <a href="{{settings.PREFIX}}/computer/{{hostname}}/{{start+1}}/{{end}}">&rarr;</a>
%end

{{! json2tree(computer1.hardware, diff=diff, lr='l' )}}
</div>
<div class="column">
<h2>Версия {{end}}<br/>{{computer2.date}}</h2>

%if end > 0:
    <a href="{{settings.PREFIX}}/computer/{{hostname}}/{{start}}/{{end-1}}">&larr;</a>
%end
&nbsp;{{end}}&nbsp;
%if end < length-1:
    <a href="{{settings.PREFIX}}/computer/{{hostname}}/{{start}}/{{end+1}}">&rarr;</a>
%end

{{! json2tree(computer2.hardware, diff=diff, lr='r' )}}
</div>
</div>

%include footer
