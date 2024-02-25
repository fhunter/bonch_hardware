%include header
%import settings
<h1>Список компьютеров</h1>
<table border=1>
<tr><th>Hostname</th><th>Date</th></tr>
%for i in computers:
<tr><td><a href="{{settings.PREFIX}}/computer/{{i.hostname}}">{{i.hostname}}</a></td><td>{{i.date}}</td></tr>
%end 
</table>
%include footer
