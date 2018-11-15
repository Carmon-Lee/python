import requests
import re
import json

if __name__ == '__main__':
    with open('tone_file.txt', 'r') as f:
        lines=f.readlines()[0]
    print(lines)
    tone_pat=re.compile(r'<td align=center>(?!\s)(.*?)</td>')
    freq_pat=re.compile(r'<td align=center>\s*?(\d.*?)</td>')

    tones=tone_pat.findall(lines)
    freqs=freq_pat.findall(lines)

    tones=[i.replace('<sub>','').replace('</sub>','').replace('<sup>','').replace('</sup>','').replace('&nbsp;','') for i in tones]
    freqs=freqs[::2]
    freqs=[float(i) for i in freqs]
    print(len(tones),tones)
    print(len(freqs),freqs)
    tone_freq_map={i:j for i,j in zip(tones,freqs)}
    with open('tone_freq_map.json', 'w') as f:
        json.dump(tone_freq_map,f)
    # tone_url = 'http://pages.mtu.edu/~suits/notefreqs.html'
    # tone_page = requests.get(tone_url)
    # with open('tone_file.txt', 'w') as f:
    #     f.write(str(tone_page.content))

