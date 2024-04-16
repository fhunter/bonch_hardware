<div class='indented'>
%width = "width=100% " if depth== 1 else ""
%subclass= "-added" if added else "-deleted" if deleted else ""
    <table {{width}} class='node{{subclass}}' summary='attributes of {{data["id"]}}'>
        <thead>
            <tr>
                <td class="first">id:</td>
                <td class='second'>
%if defined('diff') and diff and ("$update" in diff) and ("id" in diff["$update"]):
%color="lightblue"
%if lr=="l":
%color="lightgreen"
%else:
%color="tomato"
%end
                    <div class='id'><span style="background-color:{{color}}">{{data['id']}}</span></div>
%else:
                    <div class='id'>{{data['id']}}</div>
%end
                </td>
            </tr>
        </thead>
%for key, value in data.items():
%if not key in exclude:
        <tr>
            <td class="first">{{key}}: </td>
%if defined('diff') and diff and ("$update" in diff) and (key in diff["$update"]):
%color="lightblue"
%if lr=="l":
%color="lightgreen"
%else:
%color="tomato"
%end
            <td class="second"><span style="background-color:{{color}}">{{value}}</span></td>
%else:
            <td class="second">{{value}}</td>
%end
        </tr>
%end
%end
