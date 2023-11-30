#[path = "../modules/files.rs"]
mod files;

use std::env;

fn main() {
    let mut file = "test.txt".to_string();

    if let Some(arg1) = env::args().nth(1) {
        file = arg1;
    }

    let mut last = 0u32;
    let mut inc = 0;

    let mut depths = vec![0];

    if let Ok(lines) = files::read_lines(file) {
        for line in lines {
            if let Ok(ip) = line {
                let new = ip.parse::<u32>();

                if let Ok(n) = new {
                    depths.push(n);                    
                }
            }
        }
    }

    for n in &depths {
        if last != 0 {
            if n > &last {
                inc += 1;
            }
        }
        last = *n;
    }

    println!("part 1: {}", inc);

    let mut inc2 = 0;

    for (i, n) in depths.iter().enumerate() {
        if i > 3 {
        let a = depths[i -3] + depths[i -2] + depths[i - 1];
        let b = depths[i -2] + depths[i -1] + n;
        if b > a {
            inc2 += 1;
        }
    }
    }

    println!("part 2: {}", inc2);
}