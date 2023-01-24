const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */

// initlize the first value in the index 
// initilize the last value in the index
// start a while loop 
// while our low number is less than our high number 
// while we get into our while loop we want to initilize our middle value 
// then we want to check if our middle value actually equals the value we are entering so that if by some chance the numbers are in between
// then we want to check if our value is greater than the middle of our array
// if it is lower than our middle value we want to set our middle value to our new lower value 
// now well have an else case that if our value is in between these two pointers we want to set our middle value to our lower value
function binarySearch(sortedNums, searchNum) {
    let end = sortedNums.length-1 
    let start = 0 
    let middle; 
    while (start <= end) {
        middle = Math.floor ((start+end)/2)
        if (sortedNums[middle]=== searchNum) {
            return sortedNums[middle] 
            
        } else if (searchNum < sortedNums[middle]) {
            end = middle 
        }
    }   
}


// answer

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
//don't iterate throught he enntire array just mid way
function binarySearch(sortedNums, searchNum) {
    //always try to declare the variables - temp variables
    let left = 0; // beginning of the statement 
    let right = sortedNums.length - 1; // ending of the statement
    
    // different method of searching not using for loop -> while loop = they do not ezxit until they meet a certain criteria
        // do this condition til high is lower than low
    while (left <= right){ 
        let mid = Math.floor(right - left/2);
        // let mid = left + ((right - left)/2);
        if( sortedNums[mid] === searchNum){
            return true;
        }
        // is your target bigger than whatever your mid is 
        else{
            if(searchNum > sortedNums[mid]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
    }
    return false;
}

// this only works when the array is already sorted
console.log(binarySearch(nums1, searchNum1));
console.log(binarySearch(nums2, searchNum2));
console.log(binarySearch(nums3, searchNum3));