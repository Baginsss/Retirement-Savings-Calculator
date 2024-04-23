# Retirement Savings Calculator
#### Video Demo:  https://www.youtube.com/watch?v=BwyGLRHHZEQ
#### Description:
In Poland, the pension system consists of so-called three pillars, of which the first two are mandatory for every citizen. The third system is optional and has been popularized in recent years by additional schemes such as PPK, and by public concerns about future pension amounts from the first two pillars. It consists of three programs, providing various benefits:
    IKE - accumulated funds are exempt from capital gains tax
    IKZE - reduction of income tax by the value of contributions in the same calendar year. (Note: accumulated funds at the time of withdrawal during retirement are taxed at 10%)
    OIPE – same benefits as IKE
However, the most important benefit of the third pillar is an individual can invest one’s savings in any financial instrument, that one wants freely, taking full responsibility for retirement strategy. All three programs have yearly limits on how much savings you can put into your retirement accounts (for self-employed on IKZE limit is slightly higher). Overall it is similar to a Roth IRA in the USA.

The program I have built is „Retirement Savings Calculator”, which helps users navigate around the third pillar of the Polish pension system. Basically based on data, provided by the user, it estimates values of the average expected result, expected monthly pension, and total deposit. Moreover, it provides a linear graph to help users visualise how compound interest would work on his/her savings.
The program consists of two files: main.html and styles.css. Styles.css defines the styling rules for HTML elements within a web page. It contains cascading style sheet (CSS) code that specifies how various elements should appear visually, such as their colors, fonts, sizes, margins, paddings, and layout properties.. Main.html is the main program, coded in HTML and javascript. Additionally, it uses the D3 javascript library for data visualization.

It starts with the declaration of being written in HTML5, setting to the English language. In the „head” section one can find the viewport with a set width to device width, linking the stylesheet page to style.css. title of same as the name of the project, and 
import of D3 javascript library.

The body is divided into a few sections: header, main, footer and script. In the Header part, there is the title of the program (same as the project’s). In main it starts with a brief introduction to the Polish retirement system and already mentioned the third pillar. Then the table with invisible lines consists of a first column for form for the user to provide needed data, a first row which gives the user calculated results, and the rest of the table is a space for a linear chart. The user needs to provide:
Age -> Between 1 and 60, to calculate remaining time to retirement;
Gender -> M/F, in the difference in life expectancy is 13 years between men and women, which significantly impacts the amount of funds in retirement;
Status of self-employment -> As already mentioned, the limit for IKZE is slightly higher for self-employed;
Monthly savings -> how much wealth the user wants to contribute toward his/her retirement funds;
For preventing users from inputting incorrect data there is EventListener which calls for the validateInputs() function. If a user tries to submit the form with incorrect data (e.g. outside of range) or leaves a form empty, it will raise appropriate communication on the website and prevent form submission.
The calculator assumes a return rate of 7% per year but doesn't count inflation, so the outcome is in nominal value rather than real. It is based on the assumption of not de/increasing the amount of savings per year and capitalising the interest till the retirement age of 60. IKE, IKZE, and OIPE have different limits of possible savings per year, so if you exceed the limit of IKE, then the overflow will be counted as IKZE, and if you exceed the limit of IKZE, then the overflow will be counted for OIPE till the maximum limit.

Focusing on the script part, there are: already mentioned EventListener, validateInputs(), and calculate(), createChart() functions.  The calculate() function processes input data related to age, gender, savings, and other parameters to compute various financial metrics. It then updates corresponding HTML elements with the results and generates a chart based on the calculated data using the createChart() function. The latter utilizes D3.js for data visualization, creating a line chart representing savings over time based on the input data. The chart dynamically adjusts its scale and appearance based on the provided dataset, ensuring accurate and visually appealing representation.

The project overlays what I have learned from the Harvard CS50 course, especially materials from weeks 2 and 8th.
