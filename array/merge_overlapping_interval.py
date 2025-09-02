# merge overlapping intervals 
# brute force approach

def merge_overlapping_intervals(intervals):
    n = len(intervals)
    merged = []
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]
        if i > 0 and merged and merged[-1][1] >= start:
            continue
        for j in range(i + 1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
            else:
                break
        merged.append([start, end])
    return merged
def main():
    intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
    result = merge_overlapping_intervals(intervals)
    print(f"Merged intervals: {result}")
if __name__ == "__main__":
    main()


# optimal approach using sorting and merging
def merge_overlapping_intervals_optimal(intervals):
    n = len(intervals)
    ans = []
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    for i in range(n):
        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    return ans
def main_optimal():
    intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
    result = merge_overlapping_intervals_optimal(intervals)
    print(f"Merged intervals (optimal): {result}")
if __name__ == "__main__":
    main_optimal()


# meeting rooms problem

def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    if not intervals:
        return True
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
        else:
            return True
def main_meeting_rooms():
    intervals = [[0, 5], [5, 10], [15, 20]]
    result = can_attend_all_meetings(intervals)
    print(f"Can attend all meetings: {result}")
if __name__ == "__main__":
    main_meeting_rooms()