
/**
*   不修改原list
*   list,被过滤的数组，test，测试条件，接收一个参数，返回true或false
*/
function jfillter(list,test){
    var listbuff=list.concat();
    for(var i=0;listbuff!=null&&i<listbuff.length;i++){
        if(!test(listbuff[i])){
            listbuff.splice(i,1);
            i--;
        }
    }
    return listbuff;
}

/**
*深度克隆
*/
function clone(obj){
    function Clone(){}
    Clone.prototype = obj;
    var o = new Clone();
    for(var a in o){
        if(typeof o[a] == "object") {
            o[a] = clone(o[a]);
        }
    }
    return o;
}