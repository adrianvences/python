/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

const nums6 = [1,4,3,2,1,1,1,5,5,5,7,8,4,8,4,4]
const expected6 = [1,4]

const nums7 = [1,2,3,1,2,3,1,2,3]
const expected7 = []

//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    var map = {}
    for (var i = 0 ; i<nums.length;i++) 
        if (nums[i] in map) {
            map[nums[i]]++
        } else {
            map[nums[i]]=1 
        } 

    let current = []
    for (num in map) {
        if (current[0] == map[num] || current.length== 0  ) {
            current.push(num)
        console.log(current)
        }
        if (current[0]< map[num]) {
            current = [num] 
        }

    }
    return current
    
}

console.log (mode(nums6))

// chris solution 
function mode(nums) {
    let newArray = []
    let map = {}

    for(let i =0; i < nums.length;i++){
        if(nums[i] in map) {
            map[nums[i]]++
        }
        else{
            map[nums[i]] = 1
        }
    }
    let maxNum = 0;
    for (item in map) {
        if(map[item] > maxNum) {
            maxNum = map[item]
        }
    }

    for(item in map) {
        if(map[item] === maxNum) {
            newArray.push(parseInt(item))
        }
    }

    return newArray

}


console.log(mode(nums1))
console.log(mode(nums2))
console.log(mode(nums3))
console.log(mode(nums4))
console.log(mode(nums5))
console.log(mode(nums6))
console.log(mode(nums7))


// kyle instructor solution

