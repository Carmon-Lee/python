import requests
import re
import json
import time

if __name__ == '__main__':

    website_url = 'https://www.zhipin.com/job_detail/'
    li_pat = r'<li>\s*?<div class="job-primary">([\s\S]*?)</div>\s*?</li>'

    for page in range(1,2):
        query = {'query': '算法工程师',
                 'page': str(page),
                 'ka': 'page-' + str(page),
                 'scity': '101280600',
                 'industry': '',
                 'position': ''}
        heads = {'authority': 'www.zhipin.com',
                 'method': 'GET',
                 'path': '/c101280600/?query=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page=' + query[
                     'page'] + '&ka=' +
                         query['ka'],
                 'scheme': 'https',
                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'accept-encoding': 'gzip, deflate, br',
                 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                 'cache-control': 'no-cache',
                 'cookie': '_uab_collina=153978641918798136791014; _umdata=85957DF9A4B3B3E8617FB5AFF2502C92B7B36E6B5AA3616D3F49730CE016E798490DF7F0C40451D1CD43AD3E795C914C9F8CB606C4B59C15401B58EA3A56F78D; sid=sem_pz_bdpc_dasou_title; lastCity=101280600; JSESSIONID=""; __c=1544229232; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26rsv_spt%3D1%26rsv_iqid%3D0xb9524c9b0002c9c6%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D10%26rsv_sug1%3D8%26rsv_sug7%3D101%26rsv_t%3Da7d1v%252B%252BJ19p37nTUlGo9W3fkR5JrQ55C6wqOeyla99jC8x4Z8%252FEQTgKmXsja%252F2FAMrbC&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1543135185,1543135382,1543144678,1544229232; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E7%25AE%2597%25E6%25B3%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26scity%3D101280600%26industry%3D%26position%3D; __a=81448249.1534669840.1543144678.1544229232.96.9.5.5; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1544229425',
                 'pragma': 'no-cache',
                 'referer': 'https://www.zhipin.com/job_detail/?query=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&scity=101280600&industry=&position=',
                 'upgrade-insecure-requests': '1',
                 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                 }

        result = requests.request(method='get', url=website_url, params=query, headers=heads)
        # print(result.content.decode('utf-8'))
        raw_infos = re.findall(li_pat, result.content.decode('utf-8'))
        jobs = []
        for raw_info in raw_infos:
            job_detail = {'title': re.findall(r'<div class="job-title">(.*?)</div>', raw_info),
                          'salary': re.findall(r'<span class="red">(.*?)</span>', raw_info),
                          'position': re.findall(
                              r'<p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>',
                              raw_info),
                          'company': re.findall(
                              r'<div class="company-text">\s*?<h3 class="name"><a href="/gongsi/0bc562732fcf91fe3nJy.html" ka="search_list_company_31_custompage" target="_blank">(.*?)</a></h3>\s*?<p>互联网<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>\s*?</div>',
                              raw_info)
                          }

            jid = re.findall(r'data-jid="(.*?)"', raw_info)[0]
            lid = re.findall(r'data-lid="(.*?)"', raw_info)[0]
            link = 'https://www.zhipin.com/view/job/card.json?jid={0}&lid={1}'.format(jid, lid)
            # time.sleep(0.5)
            try:
                card_info = requests.request(method='get', url=link, headers=heads,timeout=5)
            except Exception as e:
                print('timeout')
            job_detail['card'] = \
                re.findall(r'<div class=\\"detail-bottom-text\\">\s*?(.*?)</div>', card_info.content.decode('utf-8'))[0]
            # print(card_info.content.decode('utf-8'))
            print(job_detail)

            jobs.append(job_detail)
        job_str = json.dumps(jobs)
        with open(str(page) + 'jobs.txt', 'w') as f:
            f.write(job_str)

    pass
