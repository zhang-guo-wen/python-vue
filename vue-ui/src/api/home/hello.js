import request from '@/utils/request'

// hello测试
export function hello() {
  return request({
    url: '/user/list',
    method: 'get'
  })
}
