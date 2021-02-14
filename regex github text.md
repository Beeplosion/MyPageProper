Steps(instructed):
1. To find the newlines and add <sp> tags upon the document

Find: `^(.+?)(\n\n)`

Replace with: '`<sp>\1</sp>\2`


a).When the dot matches all is OFF, it gives the unique issue of highlighting every text and ignoring the newline but does not highlight the entire body of text unless it is a single line of text or the last line of a whole paragraph before hitting the newline. When dot matches all is ON the problem is solved and  every body of text in its entirety is highlighted for proper tagging. In this instance dot matches, all being on is the proper choice as it lets me grab every body of text correctly to tag with `<sp>`


b). The \1 and \2 both refer to a different parentheses grouping of the find command when pulling it up for the replace with. Basically it refers to group 1 (which is meant to grab every separate  body of text using the expression (.+?)) and group 2 (the double newline, \n\n) so it basically means add `<sp>` put original  text `</sp>` then add the extra lines.

c). Done. 



2. To search for and tag stage tags around stage actions. Dot matches on? Off?

For the stage lines of text, I took a skim through the entire document  and noticed a trend of how they were organized, that being within parentheses similar to how the homework for Mulan  had them within brackets. So I took a look back at our notes for expressions and realized the escape rule was the same as for brackets (i.e. \( and \)) so I just adjusted my Mulan stage expression a bit. To sum it up:

Find: `\((.*?)\)`

Replace with: `<stage>\1</stage>`


My result was that I could find everything within the parentheses and had no issue replacing them. As for whether I turned  dot matches all off or on, I had it on since with it, I had 123 items found compared to the 122 with it marked off, a minor difference yes, but with over 100 items it made more sense to me to have more items in case one is left out I cannot easily see



3. Tag Speakers. Dot on or off?

I was able to find every speaker since I noticed they would be written in all capital letters. so I wrote:

Find: `<sp>(\w+[A-Z]:)`

Replace with: `<sp><speaker>\1</speaker>`

By doing this it found the beginning of the line (sp tag) grabbed the name of the person in all caps (\w[A-Z]) then the : and replaced it with the speaker tags in between. I could not tell if the dots affected my search since I tested with it on and off and gt the same results as far as I could tell, so I left it on. I was unsure if to keep the : or not, but to fix it all that needs to be changed is adjust the find expression to '<sp>(\w+[A-Z]):' that way the : is replaced



4. add a root tag to the entire body of text
4. 
Done by searching with 

Find: `(^.+)`

Replace with: `<root>\1</root>`

As far as I can see it's green and no issues even when I reload the document. The only touch up I added was to put a space between the root tag and the start of the document to clutter it up a bit less., and manually add the title tag at the very top of the document.