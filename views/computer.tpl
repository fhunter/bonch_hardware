%include header
%import settings
%from utils import json2tree
<h1>Аппаратура компьютера {{hostname}}</h1>
<table border=1 width=100%>
<tr><th width=10%>Дата<br/>IP</th><th>Железо</th><th></th></tr>
%j=0
%for i in computers:
<tr>
<td valign=top>
    <a id="link_{{j}}"></a>
    <a href="{{settings.PREFIX}}/computer/{{i.ip}}/{{j + start}}">{{i.date}}</a>
    <br/>{{i.ip}}<br/>
%if j > 0:
    <a href="#link_{{j-1}}">&uarr;</a>
%end
%if len(computers) > 1:
&nbsp;{{j + start}}&nbsp;
%end
%if j < len(computers)-1:
    <a href="#link_{{j+1}}">&darr;</a>
%end
</td>
<td>{{! json2tree(i.hardware)}}</td>
</tr>
%j=j+1
%end
</table>
%include footer
