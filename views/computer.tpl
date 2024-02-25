%include header
%from utils import json2tree
<h1>Аппаратура компьютера {{hostname}}</h1>
<table border=1 width=100%>
<tr><th width=10%>Дата<br/>IP</th><th>Железо</th></tr>
%for i in computers:
<tr><td valign=top>{{i.date}}<br/>{{i.ip}}</td><td>{{! json2tree(i.hardware)}}</td></tr>
%end
</table>
%include footer
