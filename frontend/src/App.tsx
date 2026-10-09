import './App.css'
import { useState } from 'react';

function App() {
  // 描述接口 JSON 中的状态取值与记录结构；这些类型不执行运行时数据校验。
  type ApplicationStatus = "applied" | "awaiting_written" | "finish_written" | "awaiting_interview" |
    "finish_interview" | "offered" | "rejected" | "stopped";

  interface Application {
    id: number,
    company_name: string,
    position_name: string,
    applied_on: string,
    status: ApplicationStatus
  }

  // 当前使用本地示例记录练习展示，尚未从后端或数据库读取。
  const application_1: Application = {
    id: 1,
    company_name: "test company 1",
    position_name: "test position 1",
    applied_on: "2026-10-09",
    status: "applied"
  }
  const application_2: Application = {
    id: 2,
    company_name: "test company 2",
    position_name: "test position 2",
    applied_on: "2026-10-09",
    status: "applied"
  }

  const the_list = [application_1, application_2];
  // const the_list: Application[] = [];
  // 每条记录转换为一个 React 元素；key 用于识别条目，内容中的 id 仅用于显示。
  const map = the_list.map((item) => { return <li key={item.id}>{item.id}, {item.company_name}, {item.position_name}, {item.applied_on}, {item.status}</li> });

  const [is_loading] = useState(false);
  const [errorMsg] = useState("");
  function renderApplicationContent() {
    if (is_loading)
      return "正在加载";
    if (!(errorMsg === ""))
      return errorMsg;
    if (the_list.length === 0)
      return "暂无投递记录";
    return <ul>{map}</ul>;
  }

  return (
    <>
      <h1> 投递记录 </h1>
      {renderApplicationContent()}
    </>

  )
}

export default App
