def calculate_processing_time(m, n, job_times):
    job_times.sort()  # 将作业处理时间按升序排序
    pipelines = [0] * m  # 初始化流水线的处理时间为0
    total_time = 0  # 总时长

    for i in range(n):
        min_pipeline = min(pipelines)  # 找到处理时间最短的流水线
        #total_time += min_pipeline  # 更新总时长
        index = pipelines.index(min_pipeline)  # 找到最短处理时间的流水线的索引
        pipelines[index] += job_times[i]  # 将当前作业分配给最短处理时间的流水线


    total_time += max(pipelines)

    return total_time


# 读取输入
m, n = map(int, input().split())
job_times = list(map(int, input().split()))

# 调用函数计算总时长
total_time = calculate_processing_time(m, n, job_times)

# 输出结果
print(total_time)