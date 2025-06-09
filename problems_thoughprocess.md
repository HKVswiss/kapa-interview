# PDF Processing: Problems, Thought Process, and Solution

## Initial Thoughts

### Problems
1. Scanned document is not read in the current setup
2. No image is completely processed
3. Name of this PDF is wrongly mentioned as `esp8266-technical_reference_en.pdf`; it is actually `21098-ESPS2WROOM-scan.pdf`

### Thought Process
1. This is not a realtime application; if there are multiple PDF readers (one for text, others for tables, images), I could ensemble them at the page level to make a clean consolidated markdown.
2. I could use an LLM to consolidate in an iterative loop.
3. It's mentioned that GPT-4.1 is used—does this have multi-modal capabilities so some questions related to images can be answered?

After fixing the PDF reader, all the paragraphs of text were corrected. All the questions have been answered, but page numbers are not coming.

---

## Final Solution and Thought Process

### Major Problems

#### 1. Scanned documents are not at all read; that's why all the questions related to `21098-ESPS2WROOM-scan.pdf` are completely unanswered.
```bash
pdf = pymupdf.open(stream=doc.raw_bytes, filetype="pdf")
markdown = pymupdf4llm.to_markdown(pdf, page_chunks=False)
```
**Solution:**
1. The above commands completely ignore the scanned documents; this is fixed by using the fitz package.
2. The initial solution was to explore the usage of the fitz package.
3. `pymupdf` processes the plain text, which is useful to create headings; this is later used for chunking, and better chunks give better retrieval.
4. Though the solution with `fitz` works most of the time, it also retrieves tables, but the table is not human-readable; this needs additional retrieval to get proper tables.

#### 2. Hybrid PDF to Markdown Converter with LLM Rendering
For every page:
- The proposed solution uses `pymupdf` for paragraphs.
- `fitz` for tables.
- The retrieved text from the above two steps, aligned, is given to LLM for proper markdown format.
- Processed files are stored in `data/processed_pages/llm`.
- This approach gives a human-readable markdown format.

#### 3. All the questions are answered, but for "What is the **maximum storage temperature** for EFM8BB3?" the model failed to retrieve the context. Even though the information is present in a table, the model failed to retrieve it; this was solved by increasing `top_k` from 3 to 5.

#### 4. Additionally, two extra flags are added to Streamlit:
- **Number of chunks to retrieve** — will be used as `top_k` in RAG
- **Use LLM refinement** — if this flag is set, the model uses LLM for refining the output from pymupdf+fitz

---

## Process
I have edited the Streamlit app to add extra variables:
1. `over_write_existing_files`: this flag will overwrite the existing markdown files
2. `processing mode`: this will have three options:
   - **basic_pymu**
     - This is the basic pymu reader (misses tables)
     - Stores processed files in `data/processed_pages/basic_pymu`
     - If `over_write_existing_files` is not set, the files created in `data/processed_pages/basic_pymu` will be used for indexing
   - **no_llm_refinement**
     - Hybrid version: pymu reader + fitz (OCR)
     - This works well
     - Stores processed files in `data/processed_pages/nollm`
     - If `over_write_existing_files` is not set, the files created in `data/processed_pages/nollm` will be used for indexing
   - **llm_refinement**
     - Hybrid version: pymu reader + fitz (OCR) + LLM refinement
     - This works well
     - Stores processed files in `data/processed_pages/llm`
     - If `over_write_existing_files` is not set, the files created in `data/processed_pages/llm` will be used for indexing

---

## Question Answers

1. **What type of equipment is B20111311?**
   -**basic_pymu:** --------
   -**no_llm_refinement:** The type of equipment for B20111311 is a Modular Approval, Wi-Fi Device.
   -**llm_refinement:** The type of equipment for B20111311 is a Modular Approval, Wi-Fi Device.

2. **When was the certificate for US0057 issued?**
   -**basic_pymu:** --------
   -**no_llm_refinement:** The certificate for US0057 was issued on 2020-11-19.
   -**llm_refinement:** The certificate for US0057 was issued on 2020-11-19.

3. **Who holds the 21098-ESPS2WROOM certificate?**
   -**basic_pymu:** --------
   -**no_llm_refinement:** The holder of the 21098-ESPS2WROOM certificate is ESPRESSIF SYSTEMS (SHANGHAI) CO., LTD., located at Suite 204, Block 2, 690 Bibo Road, Zhang Jiang Hi-Tech Park, Shanghai 201203, China.
   -**llm_refinement:** The certificate 21098-ESPS2WROOM is held by ESPRESSIF SYSTEMS (SHANGHAI) CO., LTD.

4. **Can ESP8266EX be applied to any micro-controller design as a Wi-Fi adaptor?**
   -**basic_pymu:** Yes, ESP8266EX can be applied to any micro-controller design as a Wi-Fi adaptor through SPI/SDIO or I2C/UART interfaces.
   -**no_llm_refinement:** Yes, ESP8266EX can be applied to any micro-controller design as a Wi-Fi adaptor through SPI/SDIO or I2C/UART interfaces.
   -**llm_refinement:** Yes, ESP8266EX can be applied to any micro-controller design as a Wi-Fi adaptor through SPI/SDIO or I2C/UART interfaces.

5. **What is the frequency range for ESP8266EX?**
   -**basic_pymu:** The ESP8266EX supports crystal oscillators with frequencies of 40 MHz, 26 MHz, and 24 MHz.
   -**no_llm_refinement:** The frequency range for ESP8266EX is 2.4 GHz to 2.5 GHz (2400 MHz to 2483.5 MHz).
   -**llm_refinement:** The frequency range for ESP8266EX is 2.4 GHz ~ 2.5 GHz (2400 MHz ~ 2483.5 MHz).

6. **To what pin do I connect the resistor for ESP8266EX?**
   -**basic_pymu:** The resistor mentioned in the context is connected to the flash CLK pin, which corresponds to Pin 21 (SD_CLK) of the ESP8266EX. Specifically, a 0402 resistor with an initial resistance of 200 Ω is connected in series with Pin 21 SD_CLK to reduce drive current and eliminate external interruption.
   -**no_llm_refinement:** The resistor should be connected to the ERS12K pin (Pin31) of the ESP8266EX. The external ground resistor connected to this pin requires high accuracy, with a recommended value of 12K ± 1%.
   -**llm_refinement:** You connect the resistor to the RES12K pin (Pin 31) of the ESP8266EX.

7. **What’s the flash memory of EFM8BB31F32G-D-QFP32?**
   -**basic_pymu:** The flash memory of the EFM8BB31F32G-D-QFP32 is 32 kB.
   -**no_llm_refinement:** The resistor should be connected to the ERS12K pin (Pin31) of the ESP8266EX. The external ground resistor connected to this pin requires high accuracy, with a recommended value of 12K ± 1%.
   -**llm_refinement:** The flash memory of the EFM8BB31F32G-D-QFP32 is 32 kB.

8. **What is the maximum storage temperature for EFM8BB3?**
   -**basic_pymu:** The maximum storage temperature for EFM8BB3 is 150°C.
   -**no_llm_refinement:** The maximum storage temperature for the EFM8BB3 is 150 °C.
   -**llm_refinement:** The maximum storage temperature for EFM8BB3 is 150 °C.

9. **How many multi-function I/O pins does EFM8BB3 have?**
   -**basic_pymu:** EFM8BB3 has 28 multifunction I/O pins in the QFP32 package.
   -**no_llm_refinement:** Therefore, the exact number of multifunction I/O pins for the EFM8BB3 is not specified in the given context.
   -**llm_refinement:** The EFM8BB3 has up to 29 multi-function I/O pins.

10. **What is the minimum Voltage Reference Range for DACs?**
    -**basic_pymu:** The context does not provide the minimum Voltage Reference Range for DACs.
    -**no_llm_refinement:** The minimum Voltage Reference Range for DACs is 1.15 V.
    -**llm_refinement:** The minimum Voltage Reference Range for DACs is 1.15 V.

11. **What are the different power modes for EFM8BB3?**
    -**basic_pymu:** Normal Mode, Idle Mode, Suspend Mode, Stop Mode, Shutdown Mode
    -**no_llm_refinement:** Normal, Idle, Suspend, Stop, Snooze, Shutdown
    -**llm_refinement:** Normal, Idle, Suspend, Snooze, Stop, Shutdown

---

## Observations
- **basic_pymu:** Fails to read tables; when this system is used with RAG, it sometimes produces irrelevant answers.
- **no_llm_refinement:** Is better than basic_pymu as it can process extra data and tables. Can not give all the innformation, this is not human readable so we cannot have one to one visual comparision with original pdf. 
- **llm_refinement:** Gives clean output; moreover, you have page-by-page comparison of information for reference and citing (referencing) the information.

---

## New Capabilities / TODO
- This system cannot process images; if information is in images, this cannot read it. Need some LLM with visual capabilities.
