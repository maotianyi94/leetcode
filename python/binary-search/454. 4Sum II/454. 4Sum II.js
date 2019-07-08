/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */
var fourSumCount = function(A, B, C, D) {
    var sumAB = [],sumCD = [];
    var sumAB_count = {},sumCD_count = {};
    var lenA = A.length,lenB = B.length,lenC = C.length,lenD = D.length;
    var count = 0;
    for(let i = 0;i<lenA;i++){
        for(let j = 0;j < lenB;j++){

             sumAB_count[A[i]+B[j]] = sumAB_count.hasOwnProperty(A[i]+B[j]) ? sumAB_count[A[i]+B[j]] + 1:1;
        }
    }
    for(let i = 0;i<lenC;i++){
        for(let j = 0;j < lenD;j++){
             sumCD_count[C[i]+D[j]] = sumCD_count.hasOwnProperty(C[i]+D[j]) ? sumCD_count[C[i]+D[j]] + 1:1;
        }
    }
    for(ab in sumAB_count){
        if(sumCD_count.hasOwnProperty(-1*ab)){
            count += (sumAB_count[ab] * sumCD_count[-1*ab]);
        }
    }
    return count;
};