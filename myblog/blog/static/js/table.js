/**
 * Created by Administrator on 2017/8/17.
 */

var url;
//显示编辑框
function newNews(){
$('#dlg').dialog('open').dialog('center').dialog('setTitle','新增新闻');
$('#fm').form('clear');
url = '/start/';
}
//编辑新闻
function editNews(){
var row = $('#dg').datagrid('getSelected');
console.log(row);
if (row){
    $('#dlg').dialog('open').dialog('center').dialog('setTitle','Edit News');
    $('#fm').form('load',row);
    //  ajax 编辑News 并且 通过ajax 保存到后端 SQL
    url = '/edit/'+row.news_id;
}
}
// 保存新闻
function saveNews(){
$('#fm').form('submit',{
    url: url,
    onSubmit: function(){
        return $(this).form('validate');
    },
    success: function(result){
        if (result=="save"){
           $('#dlg').dialog('close');
            $('#dg').datagrid('reload');
        }else
        if (result.errorMsg){
            $.messager.show({
                title: 'Error',
                msg: result.errorMsg
            });
        } else {
            $('#dlg').dialog('close');        // close the dialog
            $('#dg').datagrid('reload');    // reload the News data
        }
    }
});
}


//删除新闻
function destroyNews(){
var row = $('#dg').datagrid('getSelected');
console.log(row);
if (row){
    $.messager.confirm('再次确认','你确定要删除这条新闻？',function(r){
        if (r){
            $.ajax({
                url: '/remove/',
                type: 'POST',
                data: {'id':row.news_id},
                success: function(data) {
                    if (data=="REMOVE"){
                        $('#dg').datagrid('reload');
                    }
                },
                error: function(data) {alert("error")}
            });
        }
    });
}
}