#[path = "../modules/files.rs"]
mod files;

use std::env;

fn get_file() -> String {
    return if let Some(arg1) = env::args().nth(1) {
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
    let mut totals = 0;
    for (i, v) in values.iter().enumerate(){
        let p: Vec<&str> = v.split(": ").collect();
        let parts: Vec<&str> = p[1].split("; ").collect();

        let mut good = true;

        for g in parts {
            let newgood = game(g.to_string());
            if(!newgood) {
                good = false;
                break;
            }
        }
        if(good) {
            totals = totals + i + 1;
        }

    }

    println!("part 1: {}", totals);
}


fn game2(value: String) -> (u32, u32, u32) {
    let parts : Vec<&str> = value.split(", ").collect();

    let mut blue_n = 0;
    let mut red_n = 0;
    let mut green_n = 0;

    for p in parts {
        let x: Vec<&str> = p.split(' ').collect();
        let count = x[0];
        let color = x[1];

        let new = count.parse::<u32>();

        if let Ok(n) = new {
           

        if(color == "blue") {
            blue_n = n;
        } else if (color == "red") {
            red_n = n;
        }
        else if (color =="green") {
            green_n = n;
        }
    }
    }
    return (blue_n, red_n, green_n);
}


fn game(value: String) -> bool {
    let parts : Vec<&str> = value.split(", ").collect();

    for p in parts {
        let x: Vec<&str> = p.split(' ').collect();
        let count = x[0];
        let color = x[1];

        let new = count.parse::<u32>();

        if let Ok(n) = new {
           

        if(color == "blue" && n > 14) {
            return false;
        } else if (color == "red" && n > 12) {
            return false;
        }
        else if (color =="green" && n > 13) {
            return false;
        }
    }
    }
    return true;
}

fn part2(values: Vec<String>) {
    let mut totals = 0u32;

    for (i, v) in values.iter().enumerate(){
        let p: Vec<&str> = v.split(": ").collect();
        let parts: Vec<&str> = p[1].split("; ").collect();

        let mut blue_n = 0;
        let mut red_n = 0;
        let mut green_n = 0;    

        for g in parts {
            let news = game2(g.to_string());

            if(news.0 > blue_n) {
                blue_n = news.0;
            }

            if(news.1 > red_n) {
                red_n = news.1;
            }

            if(news.2 > green_n) {
                green_n = news.2;
            }
        }

        totals = totals + (blue_n * red_n * green_n);
    }

    println!("part 2: {:?}", totals);
}