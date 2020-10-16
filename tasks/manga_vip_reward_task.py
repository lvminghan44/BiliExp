from models.asyncBiliApi import asyncBiliApi
from tasks.import_once import taday
import logging

async def manga_vip_reward_task(biliapi: asyncBiliApi,
                                task_config: dict
                                ) -> None:
    if not taday in task_config["days"]:
        return
    try:
        ret = await biliapi.mangaGetVipReward()
        if(ret["code"] == 0):
            logging.info(f'{biliapi.name}: 大会员成功领取{ret["data"]["amount"]}张漫读劵')
        else:
            logging.warning(f'{biliapi.name}: 大会员领取漫读劵失败,信息为：{ret["msg"]}')
    except Exception as e: 
        logging.warning(f'{biliapi.name}: 大会员领取漫读劵异常,原因为：{str(e)}')