
## AI-Summarization-tool---Testing


Project overview
This project covers building of a simple AI-powered text summarization tool, designed to generate concise summaries from long paragraphs. 
Tested like a QA engineer, it reveals interesting challenges in AI summarization, including edge cases, information loss, and hidden failures.

## Tools in test:
	• Python
	• PyCharm
	• Gradio libraries
  	• Huggingface Model : sshleifer/distilbart-cnn-12-6

 ## Test scenario: 
 
**Verify the constistencies in the responses geenrated by AI summarization tool**
 
**Input:** Sample paragraph of text

**Output:** Short summary.

**Test 1:  When clear and structured  text is provided.**

**Expected:** Responses are consistent.

**Actual result:** Remains consistent with the text provided.

**Test 2 : When the text has slight modification in wording.**

**Expected:** Responses are consistent.

**Actual result:** Remains consistent with the modfied text provided. Summaries mostly accurate.

**Test 3 : When the long text is provided.**

**Expected:** Responses are consistent.

**Actual result:** Information loss in longer texts. Similar summaries with missing key information


## Challenges observed:

Information loss in longer texts

Similar summaries with missing key information

Edge cases that appear correct but hide subtle errors

Interactive **Gradio UI** for live testing

## Demo
Link : TBD.

