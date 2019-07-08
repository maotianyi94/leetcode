/**
 * @param {number[]} houses
 * @param {number[]} heaters
 * @return {number}
 */
/* I don't know why this case cannot pass,but I think my output is the correct answer?please help me check,thanks
Input:[25921153,510616708]
[771515668,357571490,44788124,927702196,952509530]
output:331650337
expected:153045218
    */
var findRadius = function(houses, heaters) {
    var house_r = [];
    var l_heaters = heaters.length;
    var l_houses = houses.length;
    houses.sort();
    heaters.sort();
    if(l_heaters == 1){
        return Math.max(Math.abs(heaters[0]-houses[0]),Math.abs(heaters[0] - houses[l_houses-1]));
    }
    for(let i = 0 ;i < l_houses;i++){
        var rmax = Infinity;
        var start = 0,end = l_heaters;
        if(heaters[0] >= houses[i]){
            rmax = heaters[0] - houses[i];
           }
        else if(heaters[l_heaters-1] <= houses[i]){
            rmax = houses[i] - heaters[l_heaters-1];
        }
        else{
            while(start <= end){
                mid = Math.floor((start + end)/2);
                if(heaters[mid] ==  houses[i]){
                    rmax = 0;
                    break;
                }else if(heaters[mid] > houses[i]){
                    rmax = Math.min(rmax,heaters[mid]-houses[i])
                    end = mid - 1;
                }else{
                    rmax = Math.min(rmax,houses[i]-heaters[mid])
                    start = mid + 1;
                }
            }
        }
        house_r.push(rmax)
    }
    return Math.max(...house_r);
};