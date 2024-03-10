<div class='indented'>
%width = "width=100% " if depth== 1 else ""
    <table {{width}} class='node' summary='attributes of {{data["id"]}}'>
        <thead>
            <tr>
                <td class="first">id:</td>
                <td class='second'>
                    <div class='id'>{{data['id']}}</div>
                </td>
            </tr>
        </thead>
%for key, value in data.items():
%if not key in exclude:
        <tr>
            <td class="first">{{key}}: </td>
            <td class="second">{{value}}</td>
        </tr>
%end
%end
