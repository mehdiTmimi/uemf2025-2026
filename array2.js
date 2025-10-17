function ARRAY2(){
    this.tab=[]
    this.foreach = function(callback){
        for(let i=0;i<this.tab.length;i++){
            callback(tab[i],i,tab)
        }
    }
}