
<tr>
    <td class="first">configuration:</td>
    <td class="second">
        <table summary="configuration of {{entity_id}}">

%for key, value in data.items():
            <tr>
                <td class='sub-first'>{{key}}</td>
                <td>=</td>
                <td>{{value}}</td>
            </tr>
%end
        </table>
    </td>
</tr>
