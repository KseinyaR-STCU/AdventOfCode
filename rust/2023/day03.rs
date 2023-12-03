#[path = "../modules/files.rs"]
mod files;

use std::env;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Point {
    x: usize,
    y: usize,
}

#[derive(Debug, Clone, Copy, PartialEq)]
struct Num {
    value: u32,
    start_point: Point,
    end_point: Point,
}


fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    }
    else {
        "test.txt".to_string()
    };
}

fn main() {
    let mut values = vec![];

    if let Ok(lines) = files::read_lines(get_file()) {
        for line in lines {
            if let Ok(ip) = line {
                values.push(ip);                    
            }
        }
    }

    part1(values.clone());

    part2(values);
}

fn part1(values: Vec<String>) {
    let mut nums : Vec<Num> = vec![];
    let mut syms: Vec<Point> = vec![];

    let _max_x = values.len();
    let max_y = values[0].len();

    for (i, v) in values.iter().enumerate() {
        let mut curr_num = "".to_string();
        let mut start_point = Point {x: i, y: 0};
        for (j, c) in v.chars().enumerate() {
            if(c.is_digit(10)) {
                if curr_num == "" {
                    start_point.y = j;
                }
                curr_num.push(c);
            }
            else {

                if curr_num != "" {
                    //save num with end_point
                    let end_point = Point { x: i, y: j-1};
                    let this_num = Num { value: curr_num.parse::<u32>().unwrap(), end_point: end_point, start_point: start_point};

                    nums.push(this_num);
                    //reset curr_num
                    curr_num = "".to_string();
                }

                if c != '.' {
                    let curr_point = Point {x:i, y:j};
                    syms.push(curr_point);
                }
            }
        }

        //in case a number is at the end
        if curr_num != "" {
            //save num with end_point
            let end_point = Point { x: i, y: max_y - 1};
            let this_num = Num { value: curr_num.parse::<u32>().unwrap(), end_point: end_point, start_point: start_point};

            nums.push(this_num);
            //reset curr_num
            curr_num = "".to_string();
        }
    }

    let mut total = 0;

    for n in nums.iter() {
        let length = n.end_point.y - n.start_point.y;

        let start_x = n.start_point.x;
        let mut x_s = vec![];
        if start_x > 0 {
            x_s.push(start_x - 1);
        }

        x_s.push(start_x);
        x_s.push(start_x + 1);

        let mut y_s = vec![];
        if n.start_point.y > 0 {
            y_s.push(n.start_point.y - 1);
        }
        
        y_s.push(n.end_point.y + 1);

        let mut l = 0;
        while l <= length {
            y_s.push(l + n.start_point.y);
            l = l + 1;
        }

       if is_by_symbol(x_s, y_s, syms.clone()) {
        total = total + n.value;
       }
    }

    println!("part 1: {:?}", total);
}

fn is_by_symbol(x_s: Vec<usize>, y_s: Vec<usize>, symbols: Vec<Point>) -> bool {
    for x in x_s {
        for y in y_s.clone() {
            let curr_point = Point { x: x, y: y};

            if symbols.contains(&curr_point) {
                return true;
            }
        }
    }
    return false;
}

fn part2(values: Vec<String>) {
    let mut nums : Vec<Num> = vec![];
    let mut syms: Vec<Point> = vec![];

    let _max_x = values.len();
    let max_y = values[0].len();

    for (i, v) in values.iter().enumerate() {
        let mut curr_num = "".to_string();
        let mut start_point = Point {x: i, y: 0};
        for (j, c) in v.chars().enumerate() {
            if c.is_digit(10) {
                if curr_num == "" {
                    start_point.y = j;
                }
                curr_num.push(c);
            }
            else {

                if curr_num != "" {
                    //save num with end_point
                    let end_point = Point { x: i, y: j-1};
                    let this_num = Num { value: curr_num.parse::<u32>().unwrap(), end_point: end_point, start_point: start_point};

                    nums.push(this_num);
                    //reset curr_num
                    curr_num = "".to_string();
                }

                if c == '*' {
                    let curr_point = Point {x:i, y:j};
                    syms.push(curr_point);
                }
            }
        }

        //in case a number is at the end
        if curr_num != "" {
            //save num with end_point
            let end_point = Point { x: i, y: max_y - 1};
            let this_num = Num { value: curr_num.parse::<u32>().unwrap(), end_point: end_point, start_point: start_point};

            nums.push(this_num);
            //reset curr_num
            curr_num = "".to_string();
        }
    }

    let mut total = 0;

    for s in syms.iter() {

        let start_x = s.x;
        let mut x_s = vec![];
        if start_x > 0 {
            x_s.push(start_x - 1);
        }

        x_s.push(start_x);
        x_s.push(start_x + 1);

        let mut y_s = vec![];
        if s.y > 0 {
            y_s.push(s.y - 1);
        }
        y_s.push(s.y);
        y_s.push(s.y + 1);

        let nearby_nums = count_nums(x_s, y_s, nums.clone());

        if nearby_nums.len() == 2 {
            total = total + (nearby_nums[0] * nearby_nums[1]);
        }
       
    }

    println!("part 2: {:?}", total);
 }

 
fn count_nums(x_s: Vec<usize>, y_s: Vec<usize>, nums: Vec<Num>) -> Vec<u32> {
    let mut nearby_nums = vec![];

    let mut poss_points = vec![];
    for x in x_s {
        for y in y_s.clone() {
            let curr_point = Point { x: x, y: y};

            poss_points.push(curr_point);
        }
    }

    let mut is_touching;

    for n in nums {
        is_touching = false;
        let length = n.end_point.y - n.start_point.y;

        let mut l = 0;
        while l <= length {
            let curr_point = Point { x: n.start_point.x, y: n.start_point.y + l};
            
            if poss_points.contains(&curr_point) {
                is_touching = true;
                l = 1000;
            }
            l = l + 1;
        }

        if is_touching {
            nearby_nums.push(n.value);
        }
    }

    return nearby_nums;
}