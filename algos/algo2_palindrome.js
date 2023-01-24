/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
- palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
*/

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

const str5 = "tacocat"
const expected5 = true




/**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
function isPalindrome(str) {
    for (var leftIndex = 0; leftIndex < str.length/2 ; leftIndex++){
        var rightIndex = str.length-1-leftIndex
        console.log(str[leftIndex],str[rightIndex])
        if ( str[leftIndex]!== str[rightIndex]) {
            return false
        }
    } 
    return true 
}

console.log (isPalindrome(str2))
// console.log (isPalindrome(str2))
// console.log (isPalindrome(str3))
// console.log (isPalindrome(str4))
// console.log (isPalindrome(str5))
// console.log (isPalindrome("12345"))

/*****************************************************************************/